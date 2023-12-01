from django.urls import path
from . import views

# from .middlewares.auth import auth_middleware


urlpatterns = [
    path("", views.home, name="home"),
    path("signIn/", views.signIn, name="signIn"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("order/", views.order, name="order"),
    # path("login/", login.as_view(), name="login"),
    path("trekingHiking/", views.trekingHiking, name="trekingHiking"),
    path("equipments/", views.equipments, name="equipments"),
    path("fitness/", views.fitness, name="fitness"),
    path("bags/", views.bags, name="bags"),
    path("racketSports/", views.racketSports, name="racketSports"),
    path("footwear/", views.footwear, name="footwear"),
    path("runningWalking/", views.runningWalking, name="runningWalking"),
    path("teamSports/", views.teamSports, name="teamSports"),
    path("leisureItems/", views.leisureItems, name="leisureItems"),
    path("accessories/", views.accessories, name="accessories"),
    path("assamiveProducts/", views.assamiveProducts, name="assamiveProducts"),
    path("checkPhotos/", views.checkPhotos, name="checkPhotos"),
    path("about/", views.about, name="about"),
    path("comment/", views.comment, name="comment"),
    # path("deleteOrder/", views.deleteOrder, name="deleteOrder"),
    # path("cancel_order/<int:order_id>/", views.cancel_order, name="cancel_order"),
]
