# NUVAIX GROUP | Django corporate website

This is a Python/Django rebuild of the supplied NUVAIX GROUP Next.js repository. It uses the original project's company identity and approved business-division data, with a new responsive premium-corporate interface. It does not require Node.js or npm.

**Company identity retained:** NUVAIX GROUP / NUVAIX SOLUTIONS LTD / RC 9597904  
**Brand line:** INNOVATE • BUILD • DELIVER • GROW  
**WhatsApp contact:** +234 913 216 5565

## Requirements
- Python 3.10+ (Python 3.12 recommended)
- pip
- Internet connection to install Python dependencies once

## Run locally

### Linux / macOS / WSL
```bash
cd nuvaix-django
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py check
python manage.py test
python manage.py runserver
```

### Windows PowerShell
```powershell
cd nuvaix-django
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py check
python manage.py test
python manage.py runserver
```

Open http://127.0.0.1:8000/

## Features
- Responsive corporate homepage with animated/revealed sections and mobile navigation.
- Business directory and individual pages for all 10 source-approved divisions.
- About, Technology, NUVAIX Paint, Projects, Insights, Careers, Partnerships and Contact pages.
- Site-wide WhatsApp contact link and contact-page CTA to `https://wa.me/2349132165565`.
- Validated contact form stores enquiries in Django's database; authorized staff manage them at `/admin/`.
- CSRF protection, basic secure response headers, environment-based settings, WhiteNoise static serving.
- SQLite for easy local setup; configure PostgreSQL for production scale.

## Admin
Create a superuser using `python manage.py createsuperuser`, then visit `/admin/` to manage saved enquiries. Keep the admin credentials private.

## Deployment checklist
1. Set `DJANGO_SECRET_KEY` to a securely generated random value.
2. Set `DJANGO_DEBUG=0`.
3. Set `DJANGO_ALLOWED_HOSTS` to the production hostnames.
4. Set `DJANGO_CSRF_TRUSTED_ORIGINS` to full HTTPS origins, e.g. `https://www.example.com`.
5. Configure a managed PostgreSQL database and update `DATABASES` in `config/settings.py` to use environment-driven PostgreSQL settings. Do not rely on SQLite on ephemeral hosting.
6. Build static files with `python manage.py collectstatic --noinput`; apply migrations with `python manage.py migrate`.
7. Terminate HTTPS at your hosting provider, configure backups, logging, uptime monitoring, and an appropriate privacy notice.
8. Test contact submissions and admin permissions in staging before going live.

A `Dockerfile` and `Procfile` are included as starting deployment configurations. The Dockerfile expects the database to be configured correctly for the target environment before deployment.

## Important production notes
- Contact enquiries are stored in the configured Django database; this build does not claim to email the company automatically. Configure and test an approved email provider if email notifications are required.
- Projects, careers, insights and partner listings show a clear editorial state until approved real content is available. This avoids inventing projects, awards, clients, jobs or testimonials.
- The Privacy and Terms pages are draft notices and require company/legal review before launch.
- Product packaging artwork in the source was classified as concept/placeholder material; this Django site uses an abstract CSS illustration rather than presenting that artwork as confirmed inventory.
- This is a Django migration of the corporate website's core public experience, not a one-to-one port of every original Next.js route (e.g. internal design system, individual product catalogue, course-detail pages). Review and port any additional required pages before retiring the original site.

## Tests
Run:
```bash
python manage.py check
python manage.py test
```
