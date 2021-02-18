package com.helio.app.ui.blind;

import android.content.res.Resources;
import android.graphics.Color;
import android.graphics.PorterDuff;
import android.graphics.drawable.Drawable;
import android.graphics.drawable.GradientDrawable;
import android.os.Bundle;
import android.text.InputType;
import android.util.Xml;

import androidx.annotation.DrawableRes;
import androidx.preference.EditTextPreference;
import androidx.preference.ListPreference;
import androidx.preference.Preference;
import androidx.preference.PreferenceFragmentCompat;

import com.helio.app.R;

public class SensorSettingsFragment extends PreferenceFragmentCompat {

    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.sensor_preferences, rootKey);

        EditTextPreference namePreference = findPreference("name");
        EditTextPreference ipPreference = findPreference("ip");
        ListPreference changeIconPreference = findPreference("changeIcon");
        ListPreference changeColourPreference = findPreference("changeColour");
        Preference durationPreference = findPreference("durationSensitivity");
        Preference blindControllingPreference = findPreference("blindControlling");

        //IP
        assert ipPreference != null;
        ipPreference.setOnBindEditTextListener(editText -> editText.setInputType(InputType.TYPE_CLASS_PHONE));

        //Name
        assert namePreference != null;
        namePreference.setOnBindEditTextListener(editText -> editText.setInputType(InputType.TYPE_CLASS_TEXT));

        //Display which blind it is controlling
        assert blindControllingPreference != null;
        blindControllingPreference.setSummary(new SingleBlindSettingsPreferencesFragment().blindName);



    }
}