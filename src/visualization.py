import matplotlib.pyplot as plt
import seaborn as sns
from .config import FIGURES_DIR

def save_lineplot(df, x, y, title: str, filename: str):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df, x=x, y=y, ax=ax)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    out_path = FIGURES_DIR / filename
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path
