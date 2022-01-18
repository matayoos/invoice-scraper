# Invoice Scrapper

## Routes to implement

| METHOD | ROUTE                                                    | FUNCTIONALITY                                             |
| ------ | -------------------------------------------------------- | --------------------------------------------------------- |
| _GET_  | `/invoice/page={page}&pagesize{pagesize}`                | _Get all invoices pageble_                                |
| _POST_ | `/invoice`                                               | _Register a new invoice_                                  |
| _POST_ | `/invoice/list`                                          | _Register a invoice list_                                 |
| _GET_  | `/invoice/{id}`                                          | _Get invoice by id_                                       |
| _GET_  | `/invoice/{year}/page={page}&pagesize{pagesize}`         | _Get all invoices filter by year pageble_                 |
| _GET_  | `/invoice/{year}/{month}/page={page}&pagesize{pagesize}` | _Get all invoices pageble filter by year & month pageble_ |
| _GET_  | `/invoice/{id}/items`                                    | _Get invoice items_                                       |
| _POST_ | `/category`                                              | _Create a new category_                                   |
| _GET_  | `/category`                                              | _List all categories_                                     |
| _GET_  | `/items/without-category/page={page}&pagesize{pagesize}` | _Get items without category pageble_                      |
| _PUT_  | `/item/{id}/category/{id}`                               | _Set item category_                                       |
| _GET_  | `/spends/month={month}&year={year}`                      | _Get spends by month & year_                              |
| _GET_  | `/spends/{category}/month={month}&year={year}`           | _Get spends by category filtered by month and year_       |
