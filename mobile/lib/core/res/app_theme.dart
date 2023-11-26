import 'package:flutter/material.dart';

class Themes {
  static final light = ThemeData.light().copyWith(
    useMaterial3: true,

    colorScheme: ColorScheme.fromSeed(
        seedColor: Colors.orangeAccent, primary: Colors.black, onPrimary: Colors.white,),
    textTheme: const TextTheme(
      displayLarge: TextStyle(
        color: Colors.black,
        fontSize: 20,
      ),
      displayMedium: TextStyle(
        color: Colors.black,
        fontSize: 16,
      ),
      displaySmall: TextStyle(
        color: Colors.black,
        fontSize: 12,
      ),
      labelLarge: TextStyle(
        color: Colors.black,
        fontSize: 40,
        fontWeight: FontWeight.w500,
      ),
      titleLarge: TextStyle(
        color: Colors.black,
        fontSize: 24,
        fontWeight: FontWeight.w500,
      ),
      titleSmall: TextStyle(
        color: Colors.black,
        fontSize: 10,
      ),
      headlineSmall: TextStyle(
        color: Colors.grey,
        fontSize: 8,
      ),
    ),
  );
}
