from numerology.legacy.base.model import Number
from numerology.legacy.base.model.interpretation import Interpretation

DESTINY_NUMBER_INTERPRETATION: dict[Number, Interpretation] = {
    Number.ONE: Interpretation(
        title="The Leader",
        description="People with Destiny Number 1 are born leaders and pioneers. They are independent, ambitious, and driven to create their own path in life. They possess strong willpower and innovative thinking that helps them excel in their chosen endeavors.",
        strengths="Natural leadership, creativity, innovation, independence, determination, originality",
        weaknesses="Can be domineering, stubborn, self-centered, overly competitive",
    ),
    Number.TWO: Interpretation(
        title="The Mediator",
        description="Destiny Number 2 represents harmony, cooperation and balance. These individuals excel at relationships and partnerships. They have natural diplomatic abilities and often serve as peacemakers.",
        strengths="Diplomatic, cooperative, patient, sensitive, detail-oriented, supportive",
        weaknesses="Can be oversensitive, indecisive, dependent on others, passive",
    ),
    Number.THREE: Interpretation(
        title="The Creator",
        description="Those with Destiny Number 3 are creative, expressive and optimistic souls. They have natural artistic abilities and bring joy to others through their talents and positive energy.",
        strengths="Creativity, communication skills, artistic talent, enthusiasm, charm, humor",
        weaknesses="Can be scattered, superficial, moody, critical of self and others",
    ),
    Number.FOUR: Interpretation(
        title="The Builder",
        description="Destiny Number 4 individuals are practical, reliable and hardworking. They value stability and excel at creating solid foundations through discipline and methodical effort.",
        strengths="Organized, practical, trustworthy, patient, logical, hard-working",
        weaknesses="Can be rigid, stubborn, too serious, resistant to change",
    ),
    Number.FIVE: Interpretation(
        title="The Freedom Seeker",
        description="Those with Destiny Number 5 are adventurous souls who value freedom and change. They are versatile, adaptable and bring progressive energy to all they do.",
        strengths="Adaptability, versatility, resourcefulness, quick thinking, enthusiasm",
        weaknesses="Can be restless, unreliable, scattered, overindulgent",
    ),
    Number.SIX: Interpretation(
        title="The Nurturer",
        description="Destiny Number 6 represents service, responsibility and nurturing. These individuals find fulfillment in caring for others and creating harmony in their communities.",
        strengths="Responsible, caring, protective, balanced, supportive, artistic",
        weaknesses="Can be anxious, meddling, self-righteous, overprotective",
    ),
    Number.SEVEN: Interpretation(
        title="The Seeker",
        description="Those with Destiny Number 7 are spiritual seekers and deep thinkers. They have a strong desire for knowledge and understanding of life's mysteries.",
        strengths="Analytical mind, spiritual awareness, technical skills, wisdom, dignity",
        weaknesses="Can be aloof, distant, critical, suspicious, hard to know",
    ),
    Number.EIGHT: Interpretation(
        title="The Achiever",
        description="Destiny Number 8 represents material success and personal power. These individuals have natural business sense and the ability to achieve great things.",
        strengths="Executive ability, good judgment, ambition, organization, leadership",
        weaknesses="Can be workaholic, materialistic, domineering, unforgiving",
    ),
    Number.NINE: Interpretation(
        title="The Humanitarian",
        description="Those with Destiny Number 9 are compassionate humanitarians with a global perspective. They are here to serve humanity and make a positive impact on the world.",
        strengths="Compassionate, generous, sophisticated, creative, humanitarian",
        weaknesses="Can be emotionally distant, resentful, self-pitying, scattered",
    ),
    Number.ELEVEN: Interpretation(
        title="The Illuminator",
        description="As a Master Number, 11 represents spiritual illumination and intuitive power. These individuals often serve as inspirational teachers and spiritual messengers.",
        strengths="Intuition, inspiration, idealism, creativity, sensitivity, vision",
        weaknesses="Can be anxious, highly stressed, scattered, impractical",
    ),
    Number.TWENTY_TWO: Interpretation(
        title="The Master Builder",
        description="Master Number 22 combines vision with practical ability to manifest great achievements. These individuals have the potential to create lasting impact through large-scale projects.",
        strengths="Practical vision, leadership, confidence, discipline, efficiency",
        weaknesses="Can be overwhelmed by potential, unfocused, domineering",
    ),
    Number.THIRTY_THREE: Interpretation(
        title="The Master Teacher",
        description="Master Number 33 represents the highest level of spiritual service through practical means. These individuals are here to uplift humanity through compassion and wisdom.",
        strengths="Compassion, healing abilities, wisdom, creativity, leadership",
        weaknesses="Can be burdened by responsibility, perfectionist, self-sacrificing",
    ),
    None: NotImplemented,
}
