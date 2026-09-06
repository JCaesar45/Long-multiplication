# LUXMERCE

LUXMERCE is a single-file luxury storefront with a production-shaped commerce contract.

## Product model

| Field | Type | Rule |
| --- | --- | --- |
| id | string | Stable SKU |
| name | string | Display name |
| category | string | Merchandising group |
| price | integer | Stored in cents |
| rating | number | 0.0 to 5.0 |
| scarcity | integer | 1 to 10 |
| badge | string | Empty string when absent |
| blurb | string | Short merchandising copy |

## Project structure:
```text
luxmerce/
  index.html
  README.md
  backend/
    python/
      main.py
    typescript/
      luxmerce-client.ts
    java/
      pom.xml
      src/
        main/
          java/
            com/
              luxmerce/
                LuxmerceApplication.java
                Product.java
                ProductRepository.java
                ProductController.java
                CheckoutController.java
                GlobalExceptionHandler.java
```
## Run the storefront

Open `index.html` directly in a browser.

Optional local server:

```bash
npx serve .
```

## Run the Python API

```bash
pip install fastapi uvicorn
cd backend/python
uvicorn main:app --reload --port 8000
```

Endpoints:

```text
GET  /api/products
GET  /api/products/{id}
POST /api/checkout
GET  /api/orders/{order_id}
```

## Use the TypeScript client

```ts
import { LuxmerceClient } from "./luxmerce-client";

const client = new LuxmerceClient("/api");
const products = await client.products();
```

## Run the Java API

```bash
cd backend/java
mvn spring-boot:run
```

Endpoints:

```text
GET  /api/products
GET  /api/products/{id}
POST /api/checkout
```

## Checkout rule

The client submits:

```json
{
  "name": "Operator",
  "email": "operator@example.com",
  "items": [
    {
      "id": "aurum-x1",
      "qty": 1
    }
  ],
  "total": 249000
}
```

The server recalculates `total` from the catalog and rejects mismatched payloads.


``

References:

Ecma International. (2024). *The ECMAScript 2024 language specification* (ECMA-262). https://tc39.es/ecma262/

FastAPI. (n.d.). *FastAPI documentation*. Retrieved September 7, 2026, from https://fastapi.tiangolo.com/

Microsoft. (n.d.). *TypeScript documentation*. Retrieved September 7, 2026, from https://www.typescriptlang.org/docs/

Mozilla. (n.d.). *CSS: Cascading Style Sheets*. MDN Web Docs. Retrieved September 7, 2026, from https://developer.mozilla.org/en-US/docs/Web/CSS

Mozilla. (n.d.). *HTML: HyperText Markup Language*. MDN Web Docs. Retrieved September 7, 2026, from https://developer.mozilla.org/en-US/docs/Web/HTML

Mozilla. (n.d.). *JavaScript*. MDN Web Docs. Retrieved September 7, 2026, from https://developer.mozilla.org/en-US/docs/Web/JavaScript

Python Software Foundation. (n.d.). *Python 3 documentation*. Retrieved September 7, 2026, from https://docs.python.org/3/

Spring. (n.d.). *Spring Boot*. Retrieved September 7, 2026, from https://spring.io/projects/spring-boot
