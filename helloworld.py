#!/usr/bin/python
# coding: utf8
#######################################################################
#
#   Copyright (c) 2015 Orange
#   valentin.boucher@orange.com
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Modifications of the original vIMS blueprint by Orange, for use in the 
# OPNFV vHello blueprint for the OPNFV Models project are: 
# Copyright 2016 AT&T Intellectual Property, Inc
#  
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  
# http://www.apache.org/licenses/LICENSE-2.0
#  
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
########################################################################


class helloworld:

    def __init__(self, inputs={}, orchestrator=None, logger=None):
        self.config = inputs
        self.orchestrator = orchestrator
        self.logger = logger
        self.deploy = False

    def set_orchestrator(self, orchestrator):
        self.orchestrator = orchestrator

    def set_flavor_id(self, flavor_id):
        self.config['flavor_id'] = flavor_id

    def set_image_id(self, image_id):
        self.config['image_id'] = image_id

    def set_agent_user(self, agent_user):
        self.config['agent_user'] = agent_user

    def set_external_network_name(self, external_network_name):
        self.config['external_network_name'] = external_network_name

    def set_public_domain(self, public_domain):
        self.config['public_domain'] = public_domain

    def deploy_vnf(self, blueprint, bp_name='helloworld',
                   dep_name='helloworld-opnfv'):
        if self.orchestrator:
            self.dep_name = dep_name
            error = self.orchestrator.download_upload_and_deploy_blueprint(
                blueprint, self.config, bp_name, dep_name)
            if error:
                return error

            self.deploy = True

        else:
            if self.logger:
                self.logger.error("Cloudify manager is down or not provide...")

    def undeploy_vnf(self):
        if self.orchestrator:
            if self.deploy:
                self.deploy = False
                self.orchestrator.undeploy_deployment(self.dep_name)
            else:
                if self.logger:
                    self.logger.error("Helloworld isn't already deploy...")
        else:
            if self.logger:
                self.logger.error("Cloudify manager is down or not provide...")
