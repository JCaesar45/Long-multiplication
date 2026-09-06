package com.luxmerce;

import org.springframework.stereotype.Component;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.function.Function;
import java.util.stream.Collectors;

@Component
public class ProductRepository {
    private final List<Product> products = List.of(
        new Product(
            "aurum-x1",
            "Aurum X1",
            "Hardware",
            249000,
            4.9,
            9,
            "Limited",
            "Hand-finished control console with weighted haptic dials."
        ),
        new Product(
            "noir-ledger",
            "Noir Ledger",
            "Software",
            89000,
            4.8,
            7,
            "Signature",
            "Encrypted portfolio ledger with offline audit trail."
        ),
        new Product(
            "velvet-api",
            "Velvet API",
            "Platform",
            120000,
            4.7,
            6,
            "Private",
            "Rate-shaped gateway for high-value transaction flows."
        ),
        new Product(
            "obsidian-desk",
            "Obsidian Desk",
            "Hardware",
            365000,
            5.0,
            8,
            "Atelier",
            "Carbon-stone standing desk with silent lift."
        ),
        new Product(
            "meridian-suit",
            "Meridian Suit",
            "Software",
            64000,
            4.6,
            5,
            "",
            "Executive analytics suite with cinematic reporting."
        ),
        new Product(
            "halcyon-key",
            "Halcyon Key",
            "Security",
            148000,
            4.9,
            10,
            "Vault",
            "Hardware key ceremony set with dual-custody shards."
        )
    );

    private final Map<String, Product> index = products.stream()
        .collect(Collectors.toMap(Product::id, Function.identity()));

    public List<Product> all() {
        return products;
    }

    public Optional<Product> findById(String id) {
        return Optional.ofNullable(index.get(id));
    }
}
