import sys
import os
sys.path.append(os.getcwd())
from tempest.api.workloadmgr import base
from tempest import config
from tempest import test
from oslo_log import log as logging
from tempest import tvaultconf
from tempest.api.workloadmgr.cli.config import command_argument_string
from tempest.api.workloadmgr.cli.util import cli_parser, query_data

LOG = logging.getLogger(__name__)
CONF = config.CONF

class WorkloadTest(base.BaseWorkloadmgrTest):

    credentials = ['primary']

    @classmethod
    def setup_clients(cls):
        super(WorkloadTest, cls).setup_clients()
        cls.client = cls.os.wlm_client

    @test.attr(type='smoke')
    @test.idempotent_id('9fe07175-912e-49a5-a629-5f52eeada4c9')
    def test_tvault1030_list_workloadtype(self):
        #List available workload types using CLI command
        rc = cli_parser.cli_returncode(command_argument_string.workload_type_list)
        if rc != 0:
            raise Exception("Command did not execute correctly")
        else:
            LOG.debug("Command executed correctly")
            
        wc = query_data.get_available_workload_types()
        out = cli_parser.cli_output(command_argument_string.workload_type_list)
        if (int(wc) == int(out)):
            LOG.debug("Workload type list command listed available workload types correctly")
        else:
            raise Exception ("Workload type list command did not list available workload types correctly")