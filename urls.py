# Copyright 2015 Huawei.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from openstack_dashboard.dashboards.admin.policy import views

urlpatterns = patterns('openstack_dashboard.dashboards.admin.policy.views',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^generate_rule$', views.generate_rule, name='generate_rule'),
    url(r'^show_results$', views.show_results, name='show_results'),
    #url(r'^show_results$', views.get_objects, name='get_objects'),
    url(r'^get_objects_and_attr$', views.get_objects, name='get_objects')
    #url(r'^add_ui$', db_op.add_ui, name='add_ui'),
    #url(r'^del_ui$', db_op.del_ui, name='del_ui'),
)  
