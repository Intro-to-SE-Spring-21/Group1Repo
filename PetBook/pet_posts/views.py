from flask import render_template,url_for,flash, redirect,request,Blueprint, request
from werkzeug.utils import secure_filename
from flask_login import current_user,login_required
from PetBook import db
from PetBook.models import PetPost
from PetBook.pet_posts.forms import PetPostForm

pet_posts = Blueprint('pet_posts',__name__)

@pet_posts.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form = PetPostForm()

    if form.validate_on_submit():

        pet_post = PetPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id
                             )
        db.session.add(pet_post)
        db.session.commit()
        flash("Pet Post Created")
        return redirect(url_for('core.index'))

    return render_template('create_post.html',form=form)


# int: makes sure that the pet_post_id gets passed as in integer
# instead of a string so we can look it up later.
@pet_posts.route('/<int:pet_post_id>')
def pet_post(pet_post_id):
    # grab the requested pet post by id number or return 404
    pet_post = PetPost.query.get_or_404(pet_post_id)
    return render_template('pet_post.html',title=pet_post.title,
                            date=pet_post.date,post=pet_post
    )



@pet_posts.route("/<int:pet_post_id>/update", methods=['GET', 'POST'])
@login_required
def update(pet_post_id):
    pet_post = PetPost.query.get_or_404(pet_post_id)
    if pet_post.author != current_user:
        # Forbidden, No Access
        abort(403)

    form = PetPostForm()
    if form.validate_on_submit():
        pet_post.title = form.title.data
        pet_post.text = form.text.data
        db.session.commit()
        flash('Post has been updated')
        return redirect(url_for('pet_posts.pet_post', pet_post_id=pet_post.id))
    # Pass back the old pet post information so they can start again with
    # the old text and title.
    elif request.method == 'GET':
        form.title.data = pet_post.title
        form.text.data = pet_post.text
    return render_template('create_post.html', title='Update',
                           form=form)


@pet_posts.route("/<int:pet_post_id>/delete", methods=['POST'])
@login_required
def delete_post(pet_post_id):
    pet_post = PetPost.query.get_or_404(pet_post_id)
    if pet_post.author != current_user:
        abort(403)
    db.session.delete(pet_post)
    db.session.commit()
    flash('Post has been deleted')
    return redirect(url_for('core.index'))
