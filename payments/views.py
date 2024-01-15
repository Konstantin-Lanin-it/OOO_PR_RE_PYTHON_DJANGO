import stripe
from django.http import JsonResponse
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views import View
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomeView(TemplateView):
    template_name = "payments/home.html"

    def get_context_data(self, **kwargs):
        try:
            items = Item.objects.all()
        except Exception as exc:
            print(f"Ошибка базы данных {exc}")

        context = super(HomeView, self).get_context_data(**kwargs)
        context.update(
            {
                "items": items,
            }
        )
        return context


class ItemView(TemplateView):
    template_name = "payments/item.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        try:
            item = Item.objects.get(pk=pk)
        except Exception as exc:
            print(f"Ошибка базы данных {exc}")

        context = super(ItemView, self).get_context_data(**kwargs)
        context.update(
            {"item": item, "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY}
        )
        return context


class SessionView(View):
    def post(self, request, *args, **kwargs):
        url = settings.URL
        item_id = self.kwargs["pk"]
        try:
            item = Item.objects.get(id=item_id)
        except Exception as exc:
            print(f"Ошибка базы данных {exc}")

        session = stripe.checkout.Session.create(
            metadata={"item_id": item.pk},
            mode="payment",
            success_url=url + "/success/",
            cancel_url=url + "/cancelled/",
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": item.price,
                        "product_data": {
                            "name": item.name,
                        },
                    },
                    "quantity": 1,
                },
            ],
        )
        return JsonResponse({"id": session.id})


class SuccessView(TemplateView):
    template_name = "payments/success.html"


class CancelledView(TemplateView):
    template_name = "payments/cancelled.html"
