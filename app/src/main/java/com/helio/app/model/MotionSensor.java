package com.helio.app.model;

import java.util.List;

public class MotionSensor extends Sensor {
    private String motionSensitivity;

    public MotionSensor(int id, String name, String ip, boolean active, int battery,
                        List<Integer> motorIds, String style, String motionSensitivity) {
        super(id, name, ip, active, battery, motorIds, style);
        this.motionSensitivity = motionSensitivity;
    }

    public MotionSensor(int id) {
        super(id);
    }

    public String getMotionSensitivity() {
        return motionSensitivity;
    }

    public void setMotionSensitivity(String motionSensitivity) {
        this.motionSensitivity = motionSensitivity;
    }
}
