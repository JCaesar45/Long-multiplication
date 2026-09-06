export interface Product {
  id: string;
  name: string;
  category: string;
  price: number;
  rating: number;
  scarcity: number;
  badge: string;
  blurb: string;
}

export interface CheckoutItem {
  id: string;
  qty: number;
}

export interface CheckoutPayload {
  name: string;
  email: string;
  items: CheckoutItem[];
  total: number;
}

export interface CheckoutResponse {
  orderId: string;
  status: string;
  total: number;
}

export class LuxmerceClient {
  constructor(
    private readonly baseUrl = "/api",
    private readonly timeoutMs = 8000
  ) {}

  private async request<T>(path: string, init: RequestInit = {}): Promise<T> {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), this.timeoutMs);

    try {
      const response = await fetch(`${this.baseUrl}${path}`, {
        ...init,
        signal: controller.signal,
        headers: {
          "Content-Type": "application/json",
          ...init.headers,
        },
      });

      if (!response.ok) {
        throw new Error(`Request failed: ${response.status}`);
      }

      return (await response.json()) as T;
    } finally {
      clearTimeout(timer);
    }
  }

  products(): Promise<Product[]> {
    return this.request<Product[]>("/products");
  }

  product(id: string): Promise<Product> {
    return this.request<Product>(`/products/${encodeURIComponent(id)}`);
  }

  checkout(payload: CheckoutPayload): Promise<CheckoutResponse> {
    return this.request<CheckoutResponse>("/checkout", {
      method: "POST",
      body: JSON.stringify(payload),
    });
  }
}
