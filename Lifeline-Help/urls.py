from django.conf.urls import url, include
from django.contrib import admin
from temp import urls as temp_urls
from articles import urls as article_urls
from questions import urls as question_urls
from donate import urls as donate_urls
from about import urls as about_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/' , include(temp_urls)),
    url(r'^main/' , include(article_urls)),
    url(r'^question/', include(question_urls)),
    url(r'^questions/', include(question_urls)),
    url(r'^donate/', include(donate_urls)),
    url(r'^about/', include(about_urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)