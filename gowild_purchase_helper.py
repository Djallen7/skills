#!/usr/bin/env python3
"""Frontier GoWild! pass purchase helper.

What this script does:
  - Opens a real, visible Chrome window on YOUR machine
  - Takes you straight to Frontier's GoWild signup/purchase page
  - Pre-fills your email address if it can find the field

What it deliberately does NOT do:
  - It never asks for, stores, or types your password or card details.
    You type those yourself, directly into Frontier's own page.
  - It never clicks the final purchase button. You do.

One-time setup:
    pip install playwright
    playwright install chromium

Run:
    python gowild_purchase_helper.py
"""

import re
import sys

EMAIL = "danielallen.tn@gmail.com"
SIGNUP_URL = "https://booking.flyfrontier.com/MyFrontier/GoWildSignup"
INFO_URL = "https://www.flyfrontier.com/deals/gowild-pass/"


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit(
            "Playwright is not installed. Run:\n"
            "  pip install playwright\n"
            "  playwright install chromium"
        )

    with sync_playwright() as p:
        # Prefer your real installed Chrome — Frontier's bot protection is
        # far less likely to challenge it than the bundled test browser.
        try:
            browser = p.chromium.launch(headless=False, channel="chrome")
        except Exception:
            browser = p.chromium.launch(headless=False)

        context = browser.new_context(viewport=None)
        page = context.new_page()

        print(f"Opening {SIGNUP_URL} ...")
        try:
            page.goto(SIGNUP_URL, wait_until="domcontentloaded", timeout=60_000)
        except Exception as exc:
            print(f"Signup page failed to load ({exc}); opening the info page instead.")
            page.goto(INFO_URL, wait_until="domcontentloaded", timeout=60_000)

        # Everything below is best-effort: if Frontier's page changes, the
        # browser simply stays open and you continue by hand.
        try:
            page.get_by_role("button", name=re.compile("accept", re.I)).first.click(timeout=5_000)
        except Exception:
            pass

        filled = False
        for finder in (
            lambda: page.get_by_placeholder(re.compile("email", re.I)).first,
            lambda: page.locator('input[type="email"]').first,
        ):
            try:
                finder().fill(EMAIL, timeout=5_000)
                filled = True
                print(f"Pre-filled email: {EMAIL}")
                break
            except Exception:
                continue
        if not filled:
            print("Couldn't find an email field to pre-fill — just type it yourself.")

        print()
        print("From here it's all you, in the window that just opened:")
        print("  1. Sign in (or create your FrontierMiles account).")
        print("  2. Pick the $200 GoWild pass term.")
        print("  3. Enter your payment details and click the purchase button.")
        print("  4. AFTERWARD: My Account -> GoWild -> turn OFF auto-renew,")
        print("     or Frontier will re-charge you when the pass ends in February.")
        print()
        input("Press Enter here when you're completely done, to close the browser... ")
        browser.close()


if __name__ == "__main__":
    main()
