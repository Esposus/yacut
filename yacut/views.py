from flask import flash, redirect, render_template

from . import app, db, BASE_URL
from .error_handlers import check_unique_short_url
from .forms import URLForm
from .models import URLMap
from .utils import check_symbols, get_unique_short_url


@app.route('/', methods=['GET', 'POST'])
def main_page_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('main_page.html', form=form)
    original_link = form.original_link.data
    custom_id = form.custom_id.data

    if check_unique_short_url(custom_id):
        flash(f'Имя {custom_id} уже занято!')
        return render_template('main_page.html', form=form)
    if custom_id and not check_symbols(custom_id):
        flash('Допустимы только цифры и латинские буквы!')
        return render_template('main_page.html', form=form)
    if custom_id is None:
        custom_id = get_unique_short_url()

    url = URLMap(
        original=original_link,
        short=custom_id
    )
    db.session.add(url)
    db.session.commit()
    return render_template(
        'main_page.html',
        form=form,
        short_url=BASE_URL + url.short,
        original_link=url.original
        )


@app.route('/<string:short>', methods=['GET'])
def redirect_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)
