class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable

  has_enumeration_for :user_type, create_helpers: true, create_scopes: true

  has_many :addresses, as: :addressable, dependent: :destroy

  accepts_nested_attributes_for :addresses, allow_destroy: true

  validates :email, uniqueness: true
end
