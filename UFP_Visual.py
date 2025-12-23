import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_unified_field_diagram():
    fig, ax = plt.figure(figsize=(14, 8), facecolor='white'), plt.gca()
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # --- STYLE CONFIG ---
    bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="black", lw=2)
    arrow_props = dict(facecolor='black', edgecolor='black', arrowstyle='->', lw=1.5)
    
    # --- 1. THE SOURCE (Top Left) ---
    # Representing the Spectral Code / Unity Operator
    ax.text(2, 7, "I. THE SOURCE", fontsize=14, fontweight='bold', ha='center', color='#2c3e50')
    circle = patches.Circle((2, 6), 0.8, linewidth=2, edgecolor='#8e44ad', facecolor='#f3e5f5')
    ax.add_patch(circle)
    ax.text(2, 6, "Spectral Code\n(Riemann Freqs)\n$\\Sigma = 1$", ha='center', va='center', fontsize=9)
    ax.text(2, 4.8, "The $\\mathrm{ON\\acute{U}}$ Limit\n(Stationary Frame)", ha='center', fontsize=9, style='italic', color='#555')

    # --- 2. THE LOGIC (Bottom Left) ---
    # Representing Partition Calculus
    ax.text(2, 3, "II. THE LOGIC", fontsize=14, fontweight='bold', ha='center', color='#2c3e50')
    rect = patches.FancyBboxPatch((1, 1.5), 2, 1, boxstyle="round,pad=0.1", linewidth=2, edgecolor='#2980b9', facecolor='#e3f2fd')
    ax.add_patch(rect)
    ax.text(2, 2, "Partition Calculus\nDomain: $\\mathbb{R}_{>0}$\n$a \\oslash b = a/b$", ha='center', va='center', fontsize=9)

    # --- ARROW FLOW ---
    ax.annotate("", xy=(4, 6), xytext=(2.8, 6), arrowprops=arrow_props) # Source -> Operator
    ax.annotate("", xy=(4, 2), xytext=(3, 2), arrowprops=arrow_props)   # Logic -> Operator

    # --- 3. THE MECHANISM (Center) ---
    # Representing the Breathing Operator
    ax.text(6, 7, "III. THE MECHANISM", fontsize=14, fontweight='bold', ha='center', color='#2c3e50')
    
    # The Operator Box
    box = patches.Rectangle((4.5, 3), 3, 3, linewidth=3, edgecolor='#e67e22', facecolor='#fff3e0')
    ax.add_patch(box)
    ax.text(6, 5.5, "The Breathing Operator\n$\\mathcal{O}_{\\mathrm{Onu}}$", ha='center', fontsize=11, fontweight='bold')
    ax.text(6, 4.5, "Regulates Density\n(Attention Mechanism)", ha='center', fontsize=9)
    ax.text(6, 3.5, "Conservation via $\\kappa(t)$", ha='center', fontsize=8, style='italic')

    # --- ARROW FLOW ---
    ax.annotate("", xy=(8.5, 4.5), xytext=(7.5, 4.5), arrowprops=arrow_props) # Operator -> Output

    # --- 4. THE MANIFESTATION (Right) ---
    # Representing Refraction and Wakefield
    ax.text(11, 7, "IV. MANIFESTATION", fontsize=14, fontweight='bold', ha='center', color='#2c3e50')
    
    # Coherence Pressure Area
    ax.add_patch(patches.Ellipse((11, 4.5), 3, 2, angle=0, linewidth=2, edgecolor='#27ae60', facecolor='#e8f5e9'))
    ax.text(11, 5, "Coherence Refraction\n$P_{\\mathrm{coh}}$", ha='center', fontsize=10, fontweight='bold')
    ax.text(11, 4.2, "Gravity = Refractive Gradient\nMass = $\\nabla \\cdot P_{\\mathrm{coh}}$", ha='center', fontsize=8)

    # --- 5. THE LIMIT (Bottom Right) ---
    # Representing Zayyay Floor and Proof
    ax.text(11, 3, "V. THE PROOF", fontsize=14, fontweight='bold', ha='center', color='#2c3e50')
    
    # The Floor Graph Representation
    ax.plot([9.5, 12.5], [1.5, 1.5], color='red', linewidth=3, linestyle='--')
    ax.text(11, 1.8, "The Zayyay Floor ($\\Xi$)", color='red', ha='center', fontweight='bold')
    ax.text(11, 1.2, "Prevents Singularity\nBounds Galactic Spin\n$\\Xi = 0.0041$", ha='center', fontsize=8)
    
    # Connection from Manifestation to Proof
    ax.annotate("", xy=(11, 2.2), xytext=(11, 3.5), arrowprops=dict(arrowstyle='->', lw=1.5, color='gray', linestyle='dashed'))

    # Final Titles
    plt.suptitle("THE ONU-MA'AT UNIFIED FIELD SYNTHESIS", fontsize=18, fontweight='bold', y=0.95)
    plt.title("Coalescing Spectral Code, Partition Calculus, and Refractive Gravity", fontsize=12, y=0.90)

    # Save logic (user would run this)
    # plt.savefig('Onu_Unified_Model.png', dpi=300) 
    plt.show()

create_unified_field_diagram()
