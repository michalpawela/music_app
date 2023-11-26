import 'dart:async';

import 'package:flutter/material.dart';
import 'package:mobile/core/extensions/context_extension.dart';

class SplashPage extends StatefulWidget {
  const SplashPage({Key? key}) : super(key: key);
  static const routeName = '/';

  @override
  State<SplashPage> createState() => _SplashPageState();
}

class _SplashPageState extends State<SplashPage> {
  Timer? _timer;
  void _startDelay() {
    _timer = Timer(const Duration(seconds: 3), _goNext);
  }

  void _goNext(){
    Navigator.pushReplacementNamed(context, '/home');
  }

  @override
  void initState() {
    super.initState();
    _startDelay();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: SafeArea(
        child: Center(
          child: Text(
            'Logo',
            style: context.theme.textTheme.labelLarge!
                .copyWith(color: Colors.white),
          ),
        ),
      ),
    );
  }
}
