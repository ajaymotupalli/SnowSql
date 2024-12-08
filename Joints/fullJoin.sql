select *
from call_center
    Full join catalog_returns
    on call_center.cc_call_center_sk = catalog_returns.cr_call_center_sk
-- limit 100;