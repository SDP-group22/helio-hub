package com.helio.app.networking;

import androidx.annotation.NonNull;

public class Motor {
    private int id;
    private String name;
    private String ip;
    private boolean active;
    private int level;
    private int battery;
    private int length;
    private String style;

    @NonNull
    @Override
    public String toString() {
        return "Motor w/ id=" + id;
    }

    public int getId() {
        return id;
    }
}
