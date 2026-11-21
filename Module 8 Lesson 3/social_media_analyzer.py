
import matplotlib

# Set backend before importing pyplot
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

print("=" * 55)
print("       SOCIAL MEDIA TRENDS DASHBOARD")
print("=" * 55)

# ── DATA ────────────────────────────────────────────────

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

instagram = [12400, 15300, 13800, 16200, 18900, 24100, 21500]
youtube = [8900, 9200, 11400, 10800, 13200, 17600, 16100]
twitter = [6700, 7800, 6900, 8400, 9100, 7200, 6500]
tiktok = [19200, 21400, 18700, 22800, 27300, 31500, 28900]

platforms = {
    "Instagram": (instagram, "#E1306C"),
    "YouTube": (youtube, "#FF0000"),
    "Twitter": (twitter, "#1DA1F2"),
    "TikTok": (tiktok, "#000000")
}

# ── TERMINAL SUMMARY ───────────────────────────────────

print("\nWEEKLY POST COUNTS")

print(
    f"{'Platform':<12}"
    f"{'Mon':>8}{'Tue':>8}{'Wed':>8}"
    f"{'Thu':>8}{'Fri':>8}{'Sat':>8}"
    f"{'Sun':>8}{'Total':>10}"
)

print("-" * 85)

totals = {}

for name, (data, color) in platforms.items():

    total = sum(data)
    totals[name] = total

    row = f"{name:<12}"

    for value in data:
        row += f"{value:>8,}"

    row += f"{total:>10,}"

    print(row)


# ── WEEKLY RANKINGS ────────────────────────────────────

print("\nWEEKLY POST RANKINGS")

for rank, (name, total) in enumerate(
    sorted(totals.items(), key=lambda x: -x[1]), 1
):

    bar = "#" * (total // 10000)

    print(f"{rank}. {name:<12}: {bar} ({total:,})")


# ── FIGURE SETUP ───────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(14, 9))

fig.suptitle(
    "Social Media Weekly Trends Dashboard",
    fontsize=16,
    fontweight="bold",
    y=0.98
)

fig.patch.set_facecolor("#f8f9fa")


# ── PANEL 1: LINE CHART ─────────────────────────────────

ax1 = axes[0, 0]

for name, (data, color) in platforms.items():

    ax1.plot(
        days,
        data,
        marker="o",
        linewidth=2.5,
        color=color,
        label=name
    )

ax1.set_title("Daily Post Trends (All Platforms)", fontweight="bold")
ax1.set_ylabel("Number of Posts")

ax1.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f"{int(x/1000)}K")
)

ax1.legend(loc="upper left", fontsize=8)
ax1.grid(axis="y", alpha=0.3)
ax1.set_facecolor("#ffffff")


# ── PANEL 2: BAR CHART ──────────────────────────────────

ax2 = axes[0, 1]

names = list(totals.keys())
values = list(totals.values())

colors = [platforms[name][1] for name in names]

bars = ax2.bar(
    names,
    values,
    color=colors,
    edgecolor="white",
    linewidth=1.5
)

ax2.set_title("Total Weekly Posts per Platform", fontweight="bold")
ax2.set_ylabel("Total Posts")

ax2.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f"{int(x/1000)}K")
)

for bar, value in zip(bars, values):

    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 500,
        f"{value:,}",
        ha="center",
        va="bottom",
        fontsize=9,
        fontweight="bold"
    )

ax2.set_facecolor("#ffffff")
ax2.grid(axis="y", alpha=0.3)


# ── PANEL 3: WEEKDAY VS WEEKEND ─────────────────────────

ax3 = axes[1, 0]

weekday_avg = {}
weekend_avg = {}

for name, (data, color) in platforms.items():

    weekday_avg[name] = sum(data[:5]) / 5
    weekend_avg[name] = sum(data[5:]) / 2

x = range(len(names))
width = 0.35

ax3.bar(
    [i - width / 2 for i in x],
    [weekday_avg[name] for name in names],
    width,
    label="Weekday Average",
    color=[platforms[name][1] for name in names],
    alpha=0.6
)

ax3.bar(
    [i + width / 2 for i in x],
    [weekend_avg[name] for name in names],
    width,
    label="Weekend Average",
    color=[platforms[name][1] for name in names],
    alpha=1.0
)

ax3.set_title("Weekday vs Weekend Average", fontweight="bold")

ax3.set_xticks(list(x))
ax3.set_xticklabels(names)

ax3.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f"{int(x/1000)}K")
)

ax3.legend()
ax3.set_facecolor("#ffffff")
ax3.grid(axis="y", alpha=0.3)


# ── PANEL 4: AREA CHART ─────────────────────────────────

ax4 = axes[1, 1]

ax4.fill_between(
    days,
    tiktok,
    alpha=0.4,
    color="#000000",
    label="TikTok"
)

ax4.fill_between(
    days,
    instagram,
    alpha=0.4,
    color="#E1306C",
    label="Instagram"
)

ax4.plot(days, tiktok, color="#000000", linewidth=2)
ax4.plot(days, instagram, color="#E1306C", linewidth=2)

ax4.set_title(
    "TikTok vs Instagram - Head to Head",
    fontweight="bold"
)

ax4.set_ylabel("Number of Posts")

ax4.yaxis.set_major_formatter(
    mticker.FuncFormatter(lambda x, _: f"{int(x/1000)}K")
)

ax4.legend()
ax4.set_facecolor("#ffffff")
ax4.grid(axis="y", alpha=0.3)


# ── DISPLAY AND SAVE DASHBOARD ─────────────────────────

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.savefig(
    "social_media_dashboard.png",
    dpi=150,
    bbox_inches="tight"
)

print("\nDashboard saved as: social_media_dashboard.png")

# Display all four charts
plt.show(block=True)


# ── KEY INSIGHTS ───────────────────────────────────────

top_platform = max(totals, key=totals.get)

top_day_tt = days[tiktok.index(max(tiktok))]

print("\nKEY INSIGHTS")

print(
    f"Top platform this week: "
    f"{top_platform} ({totals[top_platform]:,} posts)"
)

print(f"TikTok peaks on: {top_day_tt}")

print("All platforms show their own weekly posting trends.")

print("Twitter has the lowest weekly post count.")

print("\nCHALLENGE:")

print("1. What if Instagram drops 30% on weekends?")
print("2. Add a fifth platform: Snapchat.")
print("3. Which platform grows the most from Monday to Saturday?")