select call_center.cc_call_center_sk, catalog_sales.*
from call_center
    right join catalog_SALES
    on call_center.cc_call_center_sk = catalog_sales.cs_call_center_sk
limit 100;