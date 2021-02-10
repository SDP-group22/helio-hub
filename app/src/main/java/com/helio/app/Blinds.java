package com.helio.app;

import com.helio.app.ui.BlindIcon;

import org.jetbrains.annotations.NotNull;

public class Blinds {
    private String name;
    private BlindIcon icon;

    public Blinds(String name, BlindIcon icon){
        this.name = name;
        this.icon = icon;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BlindIcon getIcon() {
        return icon;
    }

    public void setIcon(BlindIcon icon) {
        this.icon = icon;
    }


    @NotNull
    @Override
    public String toString() {
        return "Blinds{" +
                "name='" + name + '\'' +
                ", icon='" + icon + '\'' +
                '}';
    }
}
