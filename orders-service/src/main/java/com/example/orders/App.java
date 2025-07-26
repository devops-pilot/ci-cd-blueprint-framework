package com.example.orders;

public class App {
    public String status() {
        return "Orders Service is up!";
    }

    public static void main(String[] args) {
        System.out.println(new App().status());
    }
}

