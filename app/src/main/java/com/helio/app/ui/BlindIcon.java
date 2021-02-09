package com.helio.app.ui;

import com.helio.app.R;

/**
 * Represents an icon for identifying blinds (selected by the user)
 */
public enum BlindIcon {
    WINDOW("Window", R.drawable.ic_window),
    BEDROOM("Bedroom", R.drawable.ic_bed),
    BATHROOM("Bathroom", R.drawable.ic_wash),
    KITCHEN("Kitchen", R.drawable.ic_fridge),
    SQUARE("Square", R.drawable.ic_square),
    STAR("Star", R.drawable.ic_star),
    CIRCLE("Circle", R.drawable.ic_circle),
    BOOK("Book", R.drawable.ic_book),
    CHAIR("Chair", R.drawable.ic_chair),
    COMPUTER("Computer", R.drawable.ic_computer),
    HOUSE("House", R.drawable.ic_house),
    TV("Tv", R.drawable.ic_tv);

    /**
     * Friendly name of the icon
     */
    public final String name;
    /**
     * The id of the resource of the icon
     */
    public final int id;

    BlindIcon(String name, int id) {
        this.name = name;
        this.id = id;
    }

    public static String[] getNames() {
        String[] names = new String[values().length];
        for (int i = 0; i < values().length; i++) {
            names[i] = values()[i].name;
        }
        return names;
    }

}
