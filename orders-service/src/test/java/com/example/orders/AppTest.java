package com.example.orders;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AppTest {
    @Test
    void testStatus() {
        App app = new App();
        assertEquals("Orders Service is up!", app.status());
    }
}

