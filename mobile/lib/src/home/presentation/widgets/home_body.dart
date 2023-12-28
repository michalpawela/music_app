import 'package:flutter/material.dart';
import 'package:mobile/core/extensions/context_extension.dart';
import 'package:mobile/core/res/res.dart';

class HomeBody extends StatefulWidget {
  const HomeBody({Key? key}) : super(key: key);

  @override
  State<HomeBody> createState() => _HomeBodyState();
}
class Song {
  final String title;
  final String author;
  final String imageUrl;

  Song({required this.title, required this.author, required this.imageUrl});
}
class _HomeBodyState extends State<HomeBody> {
  final PageController _pageController = PageController(initialPage: 0);
  final List<String> images = [
    Res.nathalieJane,
    Res.deanLewis,
    Res.laurenSpencer,
  ];

  final Map<int, Song> songs = {
    1: Song(title: 'NF', author: 'Author 1', imageUrl: 'url1'),
    2: Song(title: 'Song 2', author: 'Author 2', imageUrl: 'url2'),
    3: Song(title: 'Song 3', author: 'Author 3', imageUrl: 'url3'),
  };

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        SizedBox(
          height: 250,
          child: PageView.builder(
            controller: _pageController,
            itemCount: images.length,
            itemBuilder: (context, index) {
              return Image.asset(
                images[index],
                fit: BoxFit.cover,
              );
            },
          ),
        ),
        const SizedBox(
          height: 16,
        ),
        Padding(
          padding: const EdgeInsets.symmetric(
            horizontal: 16,
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Good evening Adam!',
                style: context.theme.textTheme.titleLarge!
                    .copyWith(color: Colors.white),
              ),
              const Divider(),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Popular albums',
                    style: context.theme.textTheme.titleMedium!
                        .copyWith(color: Colors.white),
                  ),
                  const SizedBox(height: 16,),
                  SizedBox(
                      height: 170,
                      width: 300,
                      child: ListView.builder(
                        scrollDirection: Axis.horizontal,
                          itemCount: songs.length,
                          itemBuilder: (context, index){
                        return Center(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Container(
                                height: 120,
                                width: 120,
                                margin: const EdgeInsets.only(bottom: 4, right: 8),
                                decoration: BoxDecoration(
                                    color: Colors.white,
                                    borderRadius: BorderRadius.circular(7.5)),
                              ),

                              Text(
                                'NF',
                                style: context.theme.textTheme.labelLarge!
                                    .copyWith(
                                    color: Colors.white,
                                    fontWeight: FontWeight.bold),
                              ),

                              Text(
                                'The search',
                                style: context.theme.textTheme.labelSmall!
                                    .copyWith(color: Colors.grey),
                              )
                            ],
                          ),
                        );
                      }),
                  )],
              ),
              Column(
                children: [
                  Text(
                    'Recommended',
                    style: context.theme.textTheme.titleLarge!
                        .copyWith(color: Colors.white),
                  ),
                  SizedBox(
                    height: 350,
                  )
                ],
              )
            ],
          ),
        )
      ],
    );
  }
}
