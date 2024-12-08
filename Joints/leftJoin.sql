-- select * from call_center;
-- select * from catalog_page;

select call_center.*, catalog_sales.cs_ship_date_sk
from call_center
    left join catalog_SALES
    on call_center.cc_call_center_sk = catalog_sales.cs_call_center_sk
-- limit 100;