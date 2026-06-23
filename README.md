<p align="center">
<img src="https://i.postimg.cc/bYT4YX0R/c523199267b1d8a7441663e728872d9e.jpg" alt="سـنـفورة ٱلـبـَنـات" width="300">
</p>

# 🤖️ سـنـفورة ٱلـبـَنـات

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python">
  <img src="https://img.shields.io/badge/aiogram-3.13.1-blue?style=flat-square&logo=telegram">
  <img src="https://img.shields.io/badge/PostgreSQL-Latest-336791?style=flat-square&logo=postgresql">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0+-green?style=flat-square">
</p>

## 📋 نبذة

**سـنـفورة ٱلـبـَنـات** هو بوت ذكي متقدم على تيليغرام مبني باستخدام **aiogram 3** و**SQLAlchemy**. يدعم شخصيات متعددة، نظام الاشتراكات، لوحة تحكم متقدمة، وتكامل مع OpenAI و Gemini.

### ✨ المميزات الرئيسية:

- 🎭 **نظام الشخصيات المتقدم**: دعم شخصيات متعددة قابلة للتخصيص
- 💬 **محادثات ذكية**: تكامل مع OpenAI و Gemini
- 📊 **لوحة تحكم كاملة**: إدارة المستخدمين والشخصيات والإحصائيات
- 🔐 **نظام الاشتراكات**: إدارة الرسائل المجانية والمدفوعة
- 🗄️ **قاعدة بيانات PostgreSQL**: تخزين آمن وموثوق
- ⚡ **معالجة غير متزامنة**: أداء عالي ومتوازي
- 🌐 **دعم عربي كامل**: واجهة وأوامر بالعربية

---

## 🚀 البدء السريع

### متطلبات النظام:

- Python 3.11+
- PostgreSQL 12+
- اتصال إنترنت

### التثبيت المحلي:

```bash
# استنساخ المستودع
git clone https://github.com/Princess-0ops/-.git
cd -

# إنشاء بيئة افتراضية
python -m venv venv
source venv/bin/activate  # أو على Windows: venv\Scripts\activate

# تثبيت المتعلقات
pip install -r pyproject.toml

# تعيين متغيرات البيئة
cp .env.example .env
# عدّل .env وأضف بيانات اعتمادك

# تشغيل البوت
python main.py
```

---

## 🐳 النشر باستخدام Docker

```bash
# بناء الصورة
docker build -t sinfora-bot:latest .

# تشغيل الحاوية
docker run -d --name sinfora-bot \
  -e BOT_TOKEN="your_token" \
  -e DATABASE_URL="postgresql+asyncpg://user:pass@host:5432/db" \
  -e API_KEY="your_api_key" \
  -e TZ="Asia/Amman" \
  sinfora-bot:latest
```

---

## 🚂 النشر على Railway

### الخطوات:

1. **إنشاء حساب على [Railway](https://railway.app)**
2. **ربط المستودع**
3. **إضافة خدمة PostgreSQL**
4. **تعيين المتغيرات البيئية**:

```
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=postgresql+asyncpg://user:password@host:5432/database
API_KEY=your_openai_api_key
OWNER_ID=your_telegram_id
TZ=Asia/Amman
MAX_CONCURRENT_TASKS=2
START_FROM_LATEST=true
```

5. **تعيين أوامر البناء والتشغيل**:
   - **Build Command**: `pip install -e .`
   - **Start Command**: `python main.py`

---

## 🔐 المتغيرات البيئية المطلوبة

| المتغير | الوصف | إلزامي |
|--------|-------|--------|
| **BOT_TOKEN** | توكن البوت من BotFather | ✅ نعم |
| **DATABASE_URL** | رابط قاعدة البيانات PostgreSQL | ✅ نعم |
| **API_KEY** | مفتاح OpenAI أو Gemini | ✅ نعم |
| **OWNER_ID** | معرف صاحب البوت | ⚠️ مستحسن |
| **ADMIN_LIST** | قائمة معرفات المسؤولين | ❌ اختياري |
| **TZ** | المنطقة الزمنية | ❌ اختياري |
| **MAX_CONCURRENT_TASKS** | الحد الأقصى للمهام المتزامنة | ❌ اختياري |
| **START_FROM_LATEST** | بدء من أحدث رسالة | ❌ اختياري |

---

## 📁 هيكل المشروع

```
.
├── main.py                 # نقطة الدخول الرئيسية
├── bot/
│   ├── config/            # إعدادات المشروع
│   ├── database/          # طبقة قاعدة البيانات
│   ├── handlers/          # معالجات الأوامر
│   ├── middlewares/       # وسيط البوت
│   ├── services/          # خدمات الأعمال
│   └── utils/             # أدوات مساعدة
├── Dockerfile             # إعدادات Docker
├── pyproject.toml         # تعريف المشروع
└── README.md             # هذا الملف
```

---

## 📊 أوامر البوت

### أوامر المستخدم:
- `/start` - بدء التفاعل مع البوت
- `/help` - الحصول على مساعدة
- `/characters` - عرض الشخصيات المتاحة
- `/chat` - بدء محادثة

### أوامر المسؤولين:
- `/admin` - لوحة التحكم
- `/broadcast` - إرسال رسالة لجميع المستخدمين
- `/stats` - إحصائيات الاستخدام

---

## 🛠️ التطوير

### متطلبات التطوير:

```bash
pip install -e ".[dev]"
```

### تشغيل الاختبارات:

```bash
pytest tests/
```

---

## 📝 السجل

انظر [CHANGELOG.md](CHANGELOG.md) للاطلاع على التحديثات السابقة.

---

## 🤝 المساهمة

نرحب بالمساهمات! يرجى:

1. عمل Fork للمستودع
2. إنشاء فرع ميزة (`git checkout -b feature/amazing-feature`)
3. Commit التعديلات (`git commit -m 'Add amazing feature'`)
4. Push إلى الفرع (`git push origin feature/amazing-feature`)
5. فتح Pull Request

---

## 📄 الترخيص

هذا المشروع مرخص تحت [GPL-3.0](LICENSE).

---

## 📧 التواصل

للأسئلة والدعم:
- 📱 Telegram: [@Princess0ops](https://t.me/Princess0ops)
- 🐛 Issues: [GitHub Issues](https://github.com/Princess-0ops/-/issues)

---

## ⭐ شكر خاص

شكراً لاستخدام **سـنـفورة ٱلـبـَنـات**! إذا أعجبك المشروع، يرجى إضافة نجمة ⭐
