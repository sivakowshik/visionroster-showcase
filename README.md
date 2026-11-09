# Visionroster.ai showcase

I'm Siva, Founder & AI Engineer at Visionroster.ai. This repo is a public window into what I'm building. The product code is private; what's here is a write-up, the architecture, and a couple of small sample files so you can see how I think and write Python.

The sample code covers occupancy counting and a staffing rule only. The full roster engine and the award and compliance checks are private and still being designed. There is no live CCTV integration here, and there is no production deployment.

## The problem

I worked in hospitality for five years at Mad Mex. Rosters were nearly always built from gut feel and last week's sheet. Some nights we were three people short during the rush; other afternoons four of us stood around waiting for orders. Managers lose hours every week fixing this by hand, and staff pay the price either way.

## What Visionroster does

Most venues already have CCTV. Visionroster is being built to use computer vision and video indexing on that existing footage to understand how busy a venue actually is: how many people are in the queue, at the counter, and in the dining area. Those counts are meant to become staffing needs.

The full roster engine would take those needs, build shifts, and check them against award and compliance rules before a manager sees them. That engine, including the award and compliance checks, is private and still being designed. It is not in this repo.

The aim is a roster based on what the cameras show is happening on the floor.

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
- No live camera connection, and no production deployment.
- Staff efficiency scoring is still being designed. I want to get it right on fairness and privacy before building it.

## Tech

Python throughout. The intended stack is object detection for people counting, a frame sampling and indexing layer, a rules-plus-optimisation roster engine, and a simple manager app. The roster engine is still being designed. See [docs/architecture.md](docs/architecture.md) for the shape of that design. The code in this repo is the occupancy count and the staffing rule only.

## Samples

`samples/` has two small, self-contained files written for this repo. They cover occupancy counting and a staffing rule only:

- `occupancy.py` counts people per zone from detection boxes, with a face-blurring step.
- `staffing_rule.py` turns an occupancy level into a suggested staff count.

From a fresh clone, install the test dependency and run the tests:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest
```

## Contact

If you'd like to see more, email kowshik.sps451@gmail.com and I can walk you through a demo.
