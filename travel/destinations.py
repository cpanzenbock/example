from flask import redirect, url_for, Blueprint, render_template
from .models import Destination, Comment
from .forms import DestinationForm, CommentForm

# Use of blue print to group routes,
# name - first argument is the blue print name
# import name - second argument - helps identify the root url for it
bp = Blueprint("destination", __name__, url_prefix="/destinations")


@bp.route("/<id>")
def show(id):
    destination = get_destination()
    # dest = destination[id]
    return render_template("destinations/show.html", destination=destination)


@bp.route("/<id>/comments", methods=["GET", "POST"])
def comments(id):
    cmtform = CommentForm()
    if cmtform.validate_on_submit():
        # Do a bunch of processing of the form data TODO
        print("We got a comment: " + cmtform.data.text)
    return redirect(url_for("destination.show", id=id))


@bp.route("/create", methods=["GET", "POST"])
def dest_create():
    destform = DestinationForm()
    if destform.validate_on_submit():
        # Do a bunch of processing of the form data TODO
        return redirect(url_for("destination.dest_create"))
    return render_template("destinations/create.html", form=destform)


def get_destination():
    # creating the description of Brazil
    b_desc = """Brazil is considered an advanced emerging economy.
   It has the ninth largest GDP in the world by nominal, and eight by PPP measures. 
   It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""
    # an image location
    image_loc = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag"
    destination = Destination("Brazil", b_desc, image_loc, "10 R$")
    # a comment
    comment = Comment(
        "Sam", "Visited during the olympics, was great", "2019-11-12 11:00:00"
    )
    destination.set_comments(comment)
    comment = Comment("Bill", "free food!", "2019-11-12 11:00:00")
    destination.set_comments(comment)
    comment = Comment("Sally", "free face masks!", "2019-11-12 11:00:00")
    destination.set_comments(comment)
    return destination
