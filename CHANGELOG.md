# Changelog

All notable changes to Mudrac will be documented in this file.

This project follows [Semantic Versioning](https://semver.org/) and the format is loosely based on [Keep a Changelog](https://keepachangelog.com/).

---

## [1.0.0] - 2026-09-09

### Added
- Initial release
- Five slash commands: `/mudrac`, `/coffee`, `/motivate-me`, `/fun-fun`, `/find-part`
- Component database with 50+ parts across 20+ categories
- Keyword-based advice for common engineering problems
- Dad jokes and engineering humor
- Socket Mode support for local development
- Response time tracking

### Changed
- Command names updated for uniqueness: `/motivate-me`, `/fun-fun`, `/find-part`
- Removed all emojis from responses

### Fixed
- Missing `chat:write` scope issue
- Channel not found error

---

## [0.1.0] - 2026-09-08

### Added
- Initial prototype
- Basic command structure
- Three commands: `/mudrac`, `/coffee`, `/find`

### Known Issues
- Limited component database (20 parts)
- Scope errors requiring reinstallation
