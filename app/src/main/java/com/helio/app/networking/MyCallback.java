package com.helio.app.networking;

import com.helio.app.model.IdComponent;

import org.jetbrains.annotations.NotNull;

import java.util.Map;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MyCallback<T extends IdComponent> implements Callback<T> {
    private final Map<Integer, T> map;

    public MyCallback(Map<Integer, T> map) {
        this.map = map;
    }

    @Override
    public void onResponse(@NotNull Call<T> call, Response<T> response) {
        T t = response.body();
        if(t != null) {
            System.out.println(call + " succeeded: " + t);
            map.put(t.getId(), t);
            System.out.println("Updated local state for " + t);
        } else {
            System.out.println("Communication error");
        }
    }

    @Override
    public void onFailure(@NotNull Call<T> call, @NotNull Throwable t) {
        System.out.println(call + " failed: " + t);
    }
}
