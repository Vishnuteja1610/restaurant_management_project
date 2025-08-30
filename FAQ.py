def faq(request):
    faqs = [
        {"question": "What are your opening hours?", "answer": "We are open from 10 AM to 10 PM daily."},
        {"question": "Do you offer home delivery?", "answer": "Yes, we provide delivery through our partners."},
        {"question": "Where are you located?", "answer": "We are located at Main Street, City Center."},
    ]
    return render(request, "faq.html", {"faqs": faqs, "page_title": "FAQ"})
