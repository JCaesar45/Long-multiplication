package com.luxmerce;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class CheckoutController {
    private final ProductRepository repository;

    public CheckoutController(ProductRepository repository) {
        this.repository = repository;
    }

    public record CheckoutItem(String id, int qty) {}

    public record CheckoutRequest(
        String name,
        String email,
        List<CheckoutItem> items,
        int total
    ) {}

    public record CheckoutResponse(
        String orderId,
        String status,
        int total
    ) {}

    @PostMapping("/checkout")
    public CheckoutResponse checkout(@RequestBody CheckoutRequest request) {
        int serverTotal = request.items()
            .stream()
            .mapToInt(item -> {
                if (item.qty() < 1 || item.qty() > 99) {
                    throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Invalid quantity");
                }

                Product product = repository.findById(item.id())
                    .orElseThrow(() -> new ResponseStatusException(HttpStatus.BAD_REQUEST, "Invalid product"));

                return product.price() * item.qty();
            })
            .sum();

        if (serverTotal != request.total()) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "Total mismatch");
        }

        return new CheckoutResponse(UUID.randomUUID().toString(), "confirmed", serverTotal);
    }
}
