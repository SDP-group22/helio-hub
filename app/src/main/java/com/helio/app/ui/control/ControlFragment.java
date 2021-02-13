package com.helio.app.ui.control;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;

import com.helio.app.R;

public class ControlFragment extends Fragment {

    private ControlViewModel controlViewModel;

    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        controlViewModel =
                new ViewModelProvider(this).get(ControlViewModel.class);
        return inflater.inflate(R.layout.fragment_home, container, false);
    }
}