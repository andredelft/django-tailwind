# Django Tailwind

## Installation

1. Install from this repository using `pip`:

   ```sh
   pip install https://github.com/andredelft/django-tailwind/tarball/master
   ```

2. Ensure you have `"django.contrib.staticfiles"` in your `INSTALLED_APPS`.

3. In the project settings, add `django_tailwind` and `django_browser_reload` to `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       ...
       "django_tailwind",
       "django_browser_reload",
   ]
   ```

4. Include the app URL’s in your root URLconf(s):

   ```python
   from django.urls import include, path

   urlpatterns = [
       ...,
       path("__reload__/", include("django_browser_reload.urls")),
   ]
   ```

   You can use another prefix if required.

5. Also in the project settings, add the middleware required for `django_browser_reload` middleware:

   ```python
   MIDDLEWARE = [
       ...
       "django_browser_reload.middleware.BrowserReloadMiddleware",
       ...
   ]
   ```

   Make sure it's listed after any middleware that encodes the response. Cf. the [`django_browser_reload` documentation](https://github.com/adamchainz/django-browser-reload).

6. In the root folder of your project, initialize the Tailwind config file and CSS entrypoint using the management command:

   ```sh
   python manage.py tailwind --init
   ```

7. Compile the output CSS file

   ```sh
   python manage.py tailwind
   ```

The config file will be located in `/tailwind.config.js`, the CSS entrypoint file in `/static/src/styles.css` and the CSS output file in `/static/dist/styles.css`. These paths can be configured in the settings file using the variables `TAILWIND_CONFIG_PATH`, `TAILWIND_STYLES_SRC_PATH` and `TAILWIND_STYLES_DIST_PATH` respectively (`pathblib.Path` objects are supported).
