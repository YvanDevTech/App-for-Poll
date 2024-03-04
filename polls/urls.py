from django.urls import include, re_path, path
from django.views.generic import TemplateView
from polls import views
from .views import upload_file


uuid4="[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}"
urlpatterns = [
    re_path(r'^$', views.home, name='home'),

    re_path(r'^redirectPage/$', views.redirect_page, name='redirectPage'),
    re_path(r'^choosePollType$', views.choose_poll_type, name='choosePollType'),
    re_path(r'^candidateCreate/('+uuid4+')/$', views.candidate_create, name='candidateCreate'),
    re_path(r'^dateCandidateCreate/('+uuid4+')/$', views.date_candidate_create, name='dateCandidateCreate'),
    
    re_path(r'^manageCandidate/('+uuid4+')/$', views.manage_candidate, name='manageCandidate'),
    
    re_path(r'^updatePoll/(' + uuid4 +')/$', views.update_voting_poll, name='updatePoll'),
    
    
    re_path(r'^deleteCandidate/('+uuid4+')/([^/]+)/$', views.delete_candidate, name='deleteCandidate'),
    re_path(r'^updateVote/('+uuid4+')/([^/]+)/$', views.update_vote, name='updateVote'),
    re_path(r'^deleteVote/('+uuid4+')/([^/]+)/$', views.delete_vote, name='deleteVote'),
    re_path(r'^deleteAnonymous/('+uuid4+')/([^/]+)/$', views.delete_anonymous, name='deleteAnonymous'),
    re_path(r'^newPoll/(?P<choice>[^/]+)/$', views.new_poll, name='newPoll'),
   
    re_path(r'^viewPoll/('+uuid4+')', views.view_poll, name='viewPoll'),
    re_path(r'^status/('+uuid4+')', views.status, name='status'),
    re_path(r'^viewPollSecret/('+uuid4+')/([^/]+)/$', views.view_poll_secret, name='viewPollSecret'),
    re_path(r'^vote/('+uuid4+')', views.vote, name='vote'),
    
    re_path(r'^invitation/('+uuid4+')/$', views.invitation, name='invitation'),
    path('upload/', upload_file, name='upload_file'),
    re_path(r'^admin/('+uuid4+')/$', views.admin_poll, name='admin'),
    re_path(r'^resetPoll/('+uuid4+')/$', views.reset_poll, name='resetPoll'),
    re_path(r'^advancedParameters/('+uuid4+')/$', views.advanced_parameters, name='advancedParameters'),
   
    re_path(r'^deleteVotingPoll/(' + uuid4 +')/$', views.delete_poll, name='deleteVotingPoll'),
    re_path(r'^certificate/('+uuid4+')', views.certificate, name='certificate'),


    re_path(r'^result/(?P<poll_id>' + uuid4 + ')/(?P<method>\d+)/$', views.result_view, name='result'),
    re_path(r'^result_borda/(?P<poll_id>' + uuid4 + ')/(?P<method>\w+)/$', views.result_borda_view, name='result_borda'),

    re_path(r'^result_approval/(?P<poll_id>[\w-]+)/(?P<method>\w+)/$', views.result_approval_view, name='result_approval'),

    re_path(r'^result_simpson/(?P<poll_id>' + uuid4 + ')/(?P<method>\w+)/$', views.result_simpson_view, name='result_simpson'),
    re_path(r'^result_copeland/(?P<poll_id>' + uuid4 + ')/(?P<method>\w+)/$', views.result_copeland_view, name='result_copeland'),
    re_path(r'^result_schulze/(?P<poll_id>' + uuid4 + ')/$', views.result_schulze_view, name='result_schulze'),
    re_path(r'^result_hare/(?P<poll_id>' + uuid4 + ')/$', views.result_hare_view, name='result_hare'),


    
    re_path(r'^scores/(?P<poll_id>[-\w]+)/(?P<method>\d+)/$', views.result_scores, name='result_scores'),
    re_path(r'^data/('+uuid4+')', views.data_page, name='data'),
    re_path(r'^allData$', TemplateView.as_view(template_name='polls/all_data.html'), name='allData'),
    re_path(r'^about$', TemplateView.as_view(template_name='polls/about.html'), name='about'),

    


]
