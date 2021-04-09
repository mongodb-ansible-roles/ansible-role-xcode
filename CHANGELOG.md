## [1.3.1](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.3.0...v1.3.1) (2021-04-09)


### Bug Fixes

* Run /usr/include task only for 10.15 ([a259587](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/a259587c732cba074975181bbdee0bb8a24e5f1f))

# [1.3.0](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.2.7...v1.3.0) (2021-04-09)


### Features

* Move async timers to variables ([8a12b93](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/8a12b93cdc8788341f82c1470f64d3005d440037))

## [1.2.7](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.2.6...v1.2.7) (2021-03-04)


### Bug Fixes

* increase timeout for xcode download task ([a65665e](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/a65665e3b744d163195fbb36aea803214a57ca56))

## [1.2.6](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.2.5...v1.2.6) (2021-03-03)


### Bug Fixes

* exclude task when app is installed ([d2c3451](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/d2c34512ab4ee3f5ec2865b798ff5ef7572c4bd9))

## [1.2.5](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.2.4...v1.2.5) (2021-03-03)


### Bug Fixes

* make read step idempotent ([4c1a717](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/4c1a7175a2ade90745fa5a829e06d37ece3ee8a7))

## [1.2.4](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.2.3...v1.2.4) (2021-03-03)


### Bug Fixes

* path ([826389c](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/826389c2a10d5b40c54f65eab2c8e3de656b6b36))

## [1.2.3](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.2.2...v1.2.3) (2021-03-03)


### Bug Fixes

* correct archive name ([458b2c8](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/458b2c80eee30e78f1fe33a53e0ff492d85d0107))

## [1.2.2](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.2.1...v1.2.2) (2021-03-02)


### Bug Fixes

* read folder name properly ([313bded](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/313bded15f1d1921b35f57b05d5a8ef8ade279c7))

## [1.2.1](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.2.0...v1.2.1) (2021-03-02)


### Bug Fixes

* correct source folder ([ea60bb0](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/ea60bb087b9d433c00c458248749f4c899c1a8a1))

# [1.2.0](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.12...v1.2.0) (2021-03-02)


### Features

* create tmp folder to handle xcpde 12 specifics ([a4dc67b](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/a4dc67bae4e79641aeba81a287f0eb9f3183c12b))

## [1.1.12](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.11...v1.1.12) (2021-03-02)


### Bug Fixes

* bump unxip timeout, since xcode 12 is failing to unxip ([50b5089](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/50b5089c1bc0cee2fdc1ef4800f7cf3606d735e8))

## [1.1.11](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.10...v1.1.11) (2021-01-14)


### Bug Fixes

* Check for the final install folder ([f26a731](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/f26a731b017e0a8b1d434f162db6af1f0da769bc))

## [1.1.10](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.9...v1.1.10) (2021-01-14)


### Bug Fixes

* Update Molecule to v3 ([932e524](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/932e5241025130bcd9d299d1c5ee6146c4dd94c6))

## [1.1.9](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.8...v1.1.9) (2020-12-04)


### Bug Fixes

* correct when condition ([46c37bb](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/46c37bb1add9af4890571cb0d4d87ab1be7e9615))

## [1.1.8](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.7...v1.1.8) (2020-12-04)


### Bug Fixes

* fix usr/include task ([ca1cd9e](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/ca1cd9ee8eb0d9dcf998091a05aa3ce4fcbac60a))

## [1.1.7](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.6...v1.1.7) (2020-12-04)


### Bug Fixes

* task code fixed ([6fb709e](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/6fb709ea8a39c2f842f387c48e66f34c2c9cc490))

## [1.1.6](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.5...v1.1.6) (2020-12-04)


### Bug Fixes

* remove molecule workflow ([cfbed28](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/cfbed288e48449460840705c5492d825d759c70c))
* set /usr/include for mac10.15 ([38ba10c](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/38ba10c8a268534c33402536e8bea4dfbc557c5c))

## [1.1.5](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.4...v1.1.5) (2019-12-12)


### Bug Fixes

* Skip unxip step to speed up role ([20a8b29](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/20a8b29f5a501cd97e5e06d062a631591b62d2cd))

## [1.1.4](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.3...v1.1.4) (2019-12-09)


### Bug Fixes

* Removed checksum check to speed up stat ([8761fc7](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/8761fc7168d217a56cf2c9e34acf0e1bdc19fb64))

## [1.1.3](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.2...v1.1.3) (2019-11-06)


### Bug Fixes

* Added async to xcode download ([3b3299c](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/3b3299c8232f527bdf6695421691f16f768d3a15))

## [1.1.2](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.1...v1.1.2) (2019-11-01)


### Bug Fixes

* Actually unxip the xcode xip file ([6902c0e](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/6902c0e7266dc982edcb03cd91fc60ecfa189a90))

## [1.1.1](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.1.0...v1.1.1) (2019-11-01)


### Bug Fixes

* xcode downloading logic and extracting logic ([11d5d51](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/11d5d51093a1318e61a519a32fd1df7df2f212c8))

# [1.1.0](https://github.com/mongodb-ansible-roles/ansible-role-xcode/compare/v1.0.0...v1.1.0) (2019-11-01)


### Bug Fixes

* Fixed version variable ([2129726](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/212972678c8f581d1df763175b0427e0431f8ffe))


### Features

* Added xcode 10.1 ([b05a7c4](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/b05a7c4f90d3d60dd7e4c634874bd280882d22cb))

# 1.0.0 (2019-10-21)


### Bug Fixes

* changed var name in template file ([6117c06](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/6117c06f1dcf32192ee8252b901677a1e8e69ce6))
* license typo ([093fbb7](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/093fbb77c5fdc591f72c4e9869673967e8292fa6))
* stat task needs sudo permissions ([26c430b](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/26c430b067ceb8ea0ef12ef841cf90cd3092ae3d))


### Features

* initial commit ([f987ccf](https://github.com/mongodb-ansible-roles/ansible-role-xcode/commit/f987ccfd2b790820fdd04394dc646d1d2f4a40d2))
