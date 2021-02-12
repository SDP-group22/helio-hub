package com.helio.app;

import com.helio.app.ui.MotorIcon;

import org.jetbrains.annotations.NotNull;

public class Blinds {
    private String name;
    private MotorIcon icon;

    public Blinds(String name, MotorIcon icon){
        this.name = name;
        this.icon = icon;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MotorIcon getIcon() {
        return icon;
    }

    public void setIcon(MotorIcon icon) {
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
