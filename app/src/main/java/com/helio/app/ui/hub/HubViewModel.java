package com.helio.app.ui.hub;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

public class HubViewModel extends ViewModel {

    private MutableLiveData<String> mText;

    public HubViewModel() {
        mText = new MutableLiveData<>();
        mText.setValue("This is hub fragment");
    }

    public LiveData<String> getText() {
        return mText;
    }
}