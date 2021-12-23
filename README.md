# Invoice Scrapper

## Routes to implement

| METHOD | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| *POST* | ```/invoice``` | _Register a new invoice_ |
| *POST* | ```/invoice/list``` | _Register a invoice list_ |
| *GET* | ```/invoice/page={page}&pagesize{pagesize}``` | _Get all invoices pageble_ |
| *GET* | ```/invoice/{year}/page={page}&pagesize{pagesize}``` | _Get all invoices filter by year pageble_ |
| *GET* |  ```/invoice/{year}/{month}/page={page}&pagesize{pagesize}``` | _Get all invoices pageble filter by year & month pageble_ |
| *GET* | ```/invoice/{id}``` | _Get invoice by id_ |
| *GET* | ```/invoice/{id}/items``` | _Get invoice items_ |
| *POST* | ```/category``` | _Create a new category_ |
| *GET* | ```/category``` | _List all categories_ |
| *GET* | ```/items/without-category/page={page}&pagesize{pagesize}```| _Get items without category pageble_ |
| *PUT* | ```/item/{id}/category/{id}``` | _Set item category_ |
| *GET* | ```/spends/mounth={month}&year={year}``` | _Get spends by month &  year_ |
| *GET* | ```/spends/{category}/mounth={month}&year={year}``` | _Get spends by category filtered by month and year_ |
