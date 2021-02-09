package com.helio.app.networking;

import androidx.annotation.NonNull;

public class Motor {
    private final int id;
    private final String name;
    private final String ip;
    private final boolean active;
    private final int level;
    private final int battery;
    private final int length;
    private final String style;

    public Motor(
            int id,
            String name,
            String ip,
            boolean active,
            int level,
            int battery,
            int length,
            String style
    ) {
        this.id = id;
        this.name = name;
        this.ip = ip;
        this.active = active;
        this.level = level;
        this.battery = battery;
        this.length = length;
        this.style = style;
    }

    @NonNull
    @Override
    public String toString() {
        return "Motor w/ id=" + id;
    }

    public int getId() {
        return id;
    }
}
