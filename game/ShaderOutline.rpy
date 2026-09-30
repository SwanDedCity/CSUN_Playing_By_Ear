# ==============================================================================
# PROFESSIONAL OPTIMIZED OUTLINE & SHADOW SHADER FOR REN'PY
# Developed by: GRIMUMU (2025)
# 
# # LICENSE:
# Free for use in both commercial and non-commercial projects.
# Attribution is required. Please credit "GRIMUMU" in your project.
#
# SUPPORT & SOCIALS:
# - Itch.io:    https://grimumu.itch.io/
# - Instagram:  https://www.instagram.com/grimumu__/
# - X/Twitter:  https://x.com/Grimumu_
# - Patreon:    https://www.patreon.com/c/Grimumu
#
# ==============================================================================
#
# A high-performance solution using fixed-cost ring sampling (16-tap).
# Specialized in clean outlines and drop-shadow effects for high-res sprites.
#
# ==============================================================================
#
# QUICK PRESETS (For beginners):
# ------------------------------
# - at outline_white_thin   (2px white border)
# - at outline_white_thick  (4px white border)
# - at outline_black_thin   (2px black border)
# - at outline_black_thick  (4px black border)
# - at shadow_soft          (Transparent black shadow, 10px offset)
# - at shadow_hard          (Solid black shadow, 10px offset)
#
# PARAMETERS GUIDE (For advanced users):
# --------------------------------------
# - width:      Thickness of the outline or shadow.
# - threshold:  Alpha sensitivity (0.0 to 1.0).
# - xoffset:    Horizontal shadow shift.
# - yoffset:    Vertical shadow shift.
# - color:      Main color of the effect.
# ==============================================================================

init python:
    renpy.register_shader("remix.optimized_outline",
        variables="""
        uniform vec2 u_model_size;
        uniform float u_width;
        uniform float u_step_start;
        uniform float u_step_end;
        uniform float u_threshold;
        uniform vec2 u_offset;
        uniform vec4 u_color;
        uniform vec4 u_far_color;
        uniform vec4 u_low_color;
        """,
        fragment_functions="""
        float check_ring(sampler2D tex, vec2 uv, vec2 px_size, float radius, float threshold) {
            float alpha = 0.0;
            float diag = radius * 0.7071;
            alpha += texture2D(tex, clamp(uv + vec2(0.0, -radius) * px_size, 0.0, 1.0)).a;
            alpha += texture2D(tex, clamp(uv + vec2(0.0, radius) * px_size, 0.0, 1.0)).a;
            alpha += texture2D(tex, clamp(uv + vec2(-radius, 0.0) * px_size, 0.0, 1.0)).a;
            alpha += texture2D(tex, clamp(uv + vec2(radius, 0.0) * px_size, 0.0, 1.0)).a;
            alpha += texture2D(tex, clamp(uv + vec2(-diag, -diag) * px_size, 0.0, 1.0)).a;
            alpha += texture2D(tex, clamp(uv + vec2(diag, -diag) * px_size, 0.0, 1.0)).a;
            alpha += texture2D(tex, clamp(uv + vec2(-diag, diag) * px_size, 0.0, 1.0)).a;
            alpha += texture2D(tex, clamp(uv + vec2(diag, diag) * px_size, 0.0, 1.0)).a;
            return step(threshold, alpha);
        }
        """,
        fragment_300="""
        vec2 pixel_size = 1.0 / u_model_size;
        vec4 current_color = texture2D(tex0, v_tex_coord);
        vec2 shadow_uv = v_tex_coord - (u_offset * pixel_size);
        
        if (current_color.a >= 0.95) {
            gl_FragColor = current_color;
        } else {
            float dist_factor = 0.0;
            float hit = 0.0;
            
            if (check_ring(tex0, shadow_uv, pixel_size, u_width * 0.33, u_threshold) > 0.5) {
                dist_factor = 0.0;
                hit = 1.0;
            } 
            else if (check_ring(tex0, shadow_uv, pixel_size, u_width * 0.66, u_threshold) > 0.5) {
                dist_factor = 0.5;
                hit = 1.0;
            }
            else if (check_ring(tex0, shadow_uv, pixel_size, u_width, u_threshold) > 0.5) {
                dist_factor = 1.0;
                hit = 1.0;
            }

            if (hit > 0.5) {
                float grad = smoothstep(u_step_start, u_step_end, dist_factor);
                vec4 out_col = mix(u_color, u_far_color, grad);
                if (dist_factor >= 0.9 && u_low_color != u_color) {
                    out_col = mix(out_col, u_low_color, 0.5);
                }
                out_col.a *= u_color.a;
                gl_FragColor = mix(out_col, current_color, current_color.a);
            } else {
                gl_FragColor = current_color;
            }
        }
        """)

transform outline(width=3.0, threshold=0.5, xoffset=0.0, yoffset=0.0, color="#FFF", far_color=None, low_color=None, step_start=0.0, step_end=1.0, mesh_pad=True):
    mesh True
    mesh_pad (False if not mesh_pad else (int(width + abs(xoffset) + 2), int(width + abs(yoffset) + 2), int(width + abs(xoffset) + 2), int(width + abs(yoffset) + 2)))
    shader "remix.optimized_outline"
    u_width float(width)
    u_threshold float(threshold)
    u_offset (float(xoffset), float(yoffset))
    u_step_start float(step_start)
    u_step_end float(step_end)
    u_color Color(color).rgba
    u_far_color (Color(far_color).rgba if far_color else Color(color).rgba)
    u_low_color (Color(low_color).rgba if low_color else Color(color).rgba)

# --- PRESETS FOR BEGINNERS ---

transform outline_white_thin:
    outline(width=2.0, color="#ffffff", threshold=0.8)

transform outline_white_thick:
    outline(width=4.0, color="#ffffff", threshold=0.8)

transform outline_black_thin:
    outline(width=2.0, color="#000000", threshold=0.8)

transform outline_black_thick:
    outline(width=4.0, color="#000000", threshold=0.8)

transform outline_red_thick:
    outline(width=4.0, color="#ff0000", threshold=0.8)


transform shadow_soft:
    outline(width=0.0, color="#00000099", xoffset=10.0, yoffset=10.0, threshold=0.4)

transform shadow_hard:
    outline(width=0.0, color="#000000", xoffset=10.0, yoffset=10.0, threshold=0.4)