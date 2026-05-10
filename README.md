# Arabela Gown Rental System

A Django-based gown rental platform for Arabela, featuring collections browsing, reservations, GCash payment, and account management.

---

## Tech Stack

- **Backend:** Django 6.0.3
- **Auth:** django-allauth
- **Frontend:** Tailwind CSS (CDN), Material Symbols, Playfair Display + Poppins fonts
- **Database:** SQLite (dev) / PostgreSQL (production via `.env`)
- **Payments:** GCash QR (manual upload)

---

## Getting Started

### 1. Activate virtual environment
```bash
venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

---

## Test Account

| Field    | Value              |
|----------|--------------------|
| Email    | test@arabela.com   |
| Password | arabela2026        |

---

## Project Structure

```
arabela-system/
├── arabela_system/       # Django project settings & URLs
├── gowns/                # Main app (views, URLs, models)
├── accounts/             # Auth (login, signup, adapters)
├── reservations/         # Reservation models & views
├── ai_recommendation/    # AI recommendation app
├── arabela_admin/        # Admin panel
├── templates/            # All HTML templates
├── static/               # CSS, JS, images
└── media/                # Uploaded files (gown photos, receipts)
```

---

## URL Map

| URL | Page |
|-----|------|
| `/` | Homepage |
| `/collections/` | All categories |
| `/wedding/` | Wedding collection |
| `/dresses/` | Dresses collection |
| `/filipiniana/` | Filipiniana collection |
| `/kid-suit/` | Kids Suit collection |
| `/suit/` | Suit collection |
| `/ball-gown/` | Ball Gown collection |
| `/collections/<category>/products/<slug>/` | Product detail |
| `/reservation/` | Checkout / reservation form |
| `/confirmation/` | Booking confirmation |
| `/reservations/` | My orders (login required) |
| `/profile/` | Account settings (login required) |
| `/about/` | About Arabela |
| `/contact/` | Contact page |
| `/terms/` | Terms and Conditions |
| `/how-it-works/` | How It Works (5 steps) |
| `/accounts/login/` | Login |
| `/accounts/signup/` | Sign up |
| `/admin/` | Django admin |
| `/admin-panel/` | Arabela custom admin |

---

## Updates Made This Session

### Template Architecture

- **Merged `home.html` into `base.html` inheritance** — removed ~800 lines of duplicated navbar, cart drawer, AI panel, and JavaScript that existed in both files. `home.html` now properly extends `base.html` using `{% block %}` tags.

---

### New Pages Created

| Page | URL | Notes |
|------|-----|-------|
| About Us | `/about/` | Two-column layout with mission, collection info, and CTA |
| Contact Us | `/contact/` | Contact info + send message form (client-side success state) |
| Terms & Conditions | `/terms/` | 7-section terms document |
| How It Works | `/how-it-works/` | 5-step editorial layout with large step numbers |
| Profile / Account | `/profile/` | Edit display name, view email, sign out, link to reservations |

---

### Navigation Bar Fixes

- **Rent dropdown** — all 6 category links now point to their dedicated pages (`/dresses/`, `/filipiniana/`, etc.) instead of filter query strings on `/collections/`
- **How it Works** — simplified to a direct link, removed the unnecessary dropdown
- **Search bar** — moved from an icon button on the right to an embedded input in the **center** of the navbar; typing in it opens and syncs with the existing search overlay
- **Search icon button** — removed from the right side icons
- **Person icon** — now redirects to `/profile/` when logged in (was incorrectly going to `/reservations/`)
- **Search overlay and AI panel** — correctly hidden on reservation and confirmation pages to avoid interfering with checkout
- **Reservation page** — full navbar with Rent links now visible (was previously hidden)

**Navbar visibility per page:**

| Element | Normal | Reservation | Confirmation |
|---------|--------|-------------|--------------|
| Logo | ✓ | ✓ | ✓ |
| Rent / How it Works | ✓ | ✓ | ✗ |
| Search bar | ✓ | ✗ | ✗ |
| AI wand | ✓ | ✗ | ✗ |
| Cart | ✓ | ✓ | ✗ |
| Person | ✓ | ✓ | ✗ |

---

### Footer Fixes

- **About us** → `/about/`
- **Contact us** → `/contact/`
- **Terms and Conditions** → `/terms/`
- **How it works** → `/how-it-works/`
- **FAQs** → `/how-it-works/`
- **Sustainability** (confirmation footer) → replaced with **About** → `/about/`

All `href="#"` dead links replaced with real URLs in both `base.html` and `home.html`.

---

### Collections Page Redesign

- Removed `max-w-[200px]` constraints — cards now fill their grid column
- Labels moved **below** the image (not overlaid on top)
- Added gradient overlay on image bottom for depth
- Arrow icon on each card that slides right on hover
- **3-column grid** on desktop (2 on mobile) with proper aspect ratios
- On mobile, the 3rd card in each row spans full width

---

### Individual Collection Pages (All 6)

Applied consistent product card improvements to `wedding.html`, `dresses.html`, `filipiniana.html`, `kid_suit.html`, `suit.html`, `ball_gown.html`:

- Image container: `bg-surface-container-high` background, `absolute inset-0` image fill (fixed distortion from old `flex` centering)
- Product name: uppercase, wider tracking, semibold
- Price: muted color, `tabular-nums` for alignment
- Info row: `flex justify-between` with a subtle top border separator

---

### Login Page Fix

- Removed `{% load socialaccount %}` and the **Sign in with Google** button
- Google OAuth was configured in `settings.py` but the `SocialApp` database record was never created, causing `DoesNotExist` crash on every login page load
- Email/password login form is untouched and works correctly

---

### Reservation Page Fixes

- **GCash Full Payment modal** — fixed self-closing `</div>` that caused the white modal box to be empty, pushing the close button, title, QR code, and download link outside the container
- **Search overlay conflict** — search bar is hidden on reservation page so it can't accidentally open over payment modals

---

### Profile Page

- Created `templates/profile.html` (was missing, causing 500 error)
- Deleted `templates/profile.htmls` (old typo file)
- Features: editable first/last name, read-only email, links to My Reservations and Sign Out

---

### Bug Fixes

| Bug | Fix |
|-----|-----|
| `profile.htmls` typo in `gowns/views.py` | Fixed to `profile.html` |
| GCash full payment modal broken | Fixed self-closing inner `div` |
| Login page crashing with `DoesNotExist` | Removed unconfigured Google OAuth button |
| Person icon going to orders page | Redirects to profile page now |
| Reservation page had no navbar | Restored navbar (kept search/AI hidden) |
| Search overlay opening over GCash modal | Search bar hidden on reservation page |

---

## Admin Access

Visit `/admin/` and log in with a superuser account.

To create a superuser:
```bash
python manage.py createsuperuser
```

---

## Environment Variables (`.env`)

```
DATABASE_NAME=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_HOST=
DATABASE_PORT=5432
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=true
DEFAULT_FROM_EMAIL=
REMEMBER_ME_AGE=1209600
```

Leave database variables empty to use SQLite locally.

---

## Notes for Developers

- **Placeholder images** — all collection and product images are placeholders. Replace `src` URLs in each collection template with actual `{{ gown.photos.url }}` once gowns are uploaded via admin.
- **Search** — the search UI is wired up but has no backend query. The search overlay shows category links only.
- **AI Recommends panel** — the occasion picker and suggestion cards are frontend-only. Connect to `/ai/` endpoint to enable real recommendations.
- **GCash QR** — static placeholder QR image. Replace with the actual Arabela GCash QR image in `reservation.html`.
