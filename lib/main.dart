import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:login_phoneno/home.dart';
import 'package:login_phoneno/otp.dart';
import 'package:login_phoneno/phone.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    initialRoute: 'phone',
    routes: {
      'phone': (context) =>MyPhone(),
      'otp': (context) => MyOtp(),
      'home': (context) => MyHome()
    },
  ));
}
