# Visionroster.ai — showcase

I'm Siva, Founder & AI Engineer at Visionroster.ai. This repo is a public window into what I'm building. The product code is private; what's here is a write-up, the architecture, and a couple of small sample files so you can see how I think and write Python.

## The problem

I worked in hospitality for five years at Mad Mex. Rosters were nearly always built from gut feel and last week's sheet. Some nights we were three people short during the rush; other afternoons four of us stood around waiting for orders. Managers lose hours every week fixing this by hand, and staff pay the price either way.

## What Visionroster does

Most venues already have CCTV. Visionroster uses computer vision and video indexing on that existing footage to understand how busy the venue actually is — how many people are in the queue, at the counter, in the dining area — and turns that into staffing needs. Those needs feed an AI roster engine that builds shifts and checks them against award and compliance rules before a manager sees them.

So the roster comes from what the cameras show is happening on the floor, not just from a sales spreadsheet.

## Privacy by design

Filming people at work is sensitive, and I treat it that way from the start:

- Faces are blurred and people are reduced to anonymous boxes as early as possible in the pipeline.
- The system stores counts and activity summaries, not identities.
- Raw footage isn't kept by Visionroster beyond what processing needs.
- The design is built with the Australian Privacy Act and Victoria's workplace surveillance rules in mind, and venues remain responsible for notices and consent.

This isn't legal advice, and each pilot venue will review it with their own advisers.

## Where it's at (honestly)

- Pre-revenue.
- Preparing a pilot with a pizza shop across two locations.
- Staff efficiency scoring is still being designed — I want to get it right on fairness and privacy before building it.

## Tech

Python throughout. Object detection for people counting, a frame sampling and indexing layer, a rules-plus-optimisation roster engine, and a simple manager app. See [docs/architecture.md](docs/architecture.md).

## Samples

`samples/` has two small, self-contained files written for this repo (not taken from the product):

- `occupancy.py` — counts people per zone from detection boxes, with a face-blurring step.
- `staffing_rule.py` — turns an occupancy level into a suggested staff count.

Run the tests:

```bash
pip install pytest
pytest
```

## Contact

If you'd like to see more, get in touch and I can walk you through a demo.
