package com.luxmerce;

public record Product(
    String id,
    String name,
    String category,
    int price,
    double rating,
    int scarcity,
    String badge,
    String blurb
) {}
