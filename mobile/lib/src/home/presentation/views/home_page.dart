import 'package:flutter/material.dart';
import 'package:mobile/core/common/widgets/gradient_background.dart';
import 'package:mobile/core/res/res.dart';
import 'package:mobile/src/home/presentation/widgets/home_body.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);
  static const routeName = '/home';

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      backgroundColor: Colors.white,
      extendBodyBehindAppBar: true,
      body: GradientBackground(
        image: Res.gradientBackground,
        child: HomeBody(),
      ),
    );
  }
}
